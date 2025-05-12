#include "hashMap.h"
#include "dllist.h"
#include <string.h>

/* Computes the hash value corresponding the key */
unsigned long long hash(char* key)
{
  const int p = 31;
  const int m = 1e9 + 9;
  unsigned long long hash_value = 0;
  long long p_pow = 1;
  for (int i = 0; i < strlen(key); i++) {
    char c = key[i];
    hash_value = (hash_value + (c - 'a' + 1) * p_pow) % m;
    p_pow = (p_pow * p) % m;
  }
  return hash_value;
}

void initHashMap(HashMap* hm, unsigned int nb)
{
  /* TODO: 
    * Set the numBuckets and numItems fields of hm. Intitally the hash map has 0 items.
    * Allocate memory for nb buckets, allocate memory for a DLList for each bucket, initialize the list, and initialize the bucket's lock. 
    * Initialize the tableLock.
   */
  hm->numBuckets = nb;
  hm->numItems = 0;
  hm->buckets = malloc(nb * sizeof(Bucket));
  for (int i = 0; i < nb; ++i) {
    hm->buckets[i].list = malloc(sizeof(DLList));
    initList(hm->buckets[i].list);
    pthread_mutex_init(&hm->buckets[i].lock, NULL);
  }
  pthread_mutex_init(&hm->tableLock, NULL);
}

void destroyHashMap(HashMap* hm)
{
    /* TODO: 
    * Free up each bucket and the hash map. Destroy all the mutexes. 
    * Set the numBuckets and numItems fields to zero. 
   */
  for (int i = 0; i < hm->numBuckets; ++i) {
    pthread_mutex_destroy(&hm->buckets[i].lock);
    destroyList(hm->buckets[i].list);
    free(hm->buckets[i].list);
  }
  free(hm->buckets);
  hm->numItems = 0, hm->numBuckets = 0;
  pthread_mutex_destroy(&hm->tableLock);
}

void insertHashMap(HashMap* hm, char* key, char* value)
{
  unsigned int h = hash(key) % hm->numBuckets;
  /* TODO: 
    * Go to bucket h, and insert the (key, value) pair, unless the key is already in the hash map. Note that only one thread may access bucket h at any point in time.
    * If you inserted the pair, increment the hash map's numItems field (under mutex protection, of course!)
   */
  pthread_mutex_lock(&hm->buckets[h].lock);
  int inserted = insertSortedList(hm->buckets[h].list, key, value);
  pthread_mutex_unlock(&hm->buckets[h].lock);
  if (inserted) {
    pthread_mutex_lock(&hm->tableLock);
    ++hm->numItems;
    pthread_mutex_unlock(&hm->tableLock);
  }
}

char* retrieveValue(HashMap* hm, char* key)
{
  unsigned int h = hash(key) % hm->numBuckets;
  /* TODO: 
    * Find the key in bucket h, under mutex protection. Since the bucket's key-value pairs are stored in a DLList, look at the DLList.h file for an appropriate function to get the value corresponding to the key.
   */
  pthread_mutex_lock(&hm->buckets[h].lock);
  char* value = getValue(hm->buckets[h].list, key);
  pthread_mutex_unlock(&hm->buckets[h].lock);
  return value;
}

void deleteEntry(HashMap* hm, char* key)
{
  unsigned int h = hash(key) % hm->numBuckets;
  /* TODO: 
    * Delete the key from bucket h, under mutex protection. If they key isn't in the bucket, don't do anything. 
    * If the key was successfully removed from the bucket, decrement the hashmap's numItems field. 
   */
  pthread_mutex_lock(&hm->buckets[h].lock);
  int removed = removeFromList(hm->buckets[h].list, key);
  pthread_mutex_unlock(&hm->buckets[h].lock);
  if (removed) {
    pthread_mutex_lock(&hm->tableLock);
    --hm->numItems;
    pthread_mutex_unlock(&hm->tableLock);
  }
}


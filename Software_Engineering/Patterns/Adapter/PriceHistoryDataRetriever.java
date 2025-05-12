package Patterns.Adapter;

public class PriceHistoryDataRetriever implements DataRetriever{
    private String data = "23.50,34.25,25.99";
    public PriceHistoryDataRetriever() {}
    @Override
    public String getData() {
        return data;
    }
}

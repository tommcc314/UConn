export default async function handler(req, res) {
  const apiKey = process.env.GOOGLE_FONTS_KEY;

  if (!apiKey) {
    return res.status(500).json({ error: "API key not configured" });
  }

  const { font } = req.query;
  const googleFontsUrl = `https://www.googleapis.com/webfonts/v1/webfonts?key=${apiKey}`;

  try {
    const response = await fetch(googleFontsUrl);
    const data = await response.json();
    res.status(200).json(data);
  } catch (error) {
    res.status(500).json({ error: "Failed to fetch Google Fonts data" });
  }  
}
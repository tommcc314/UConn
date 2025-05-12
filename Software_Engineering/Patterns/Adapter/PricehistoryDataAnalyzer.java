package Patterns.Adapter;
import java.util.List;
import java.util.ArrayList;
public class PricehistoryDataAnalyzer implements DataAnalyzer{
    private DataRetriever priceHistory;
    private NumericalDataAnalyzer analyzer = new NumericalDataAnalyzer();
    public PricehistoryDataAnalyzer(DataRetriever priceHistory) {
        this.priceHistory = priceHistory;
    }
    public double mean() {
        String[] prices = (priceHistory.getData()).split(",");
        List<Double> data = new ArrayList<Double>();
        for (String price : prices) {
            data.add(Double.parseDouble(price));
        }
        analyzer.setData(data);
        return analyzer.mean();
    }
}

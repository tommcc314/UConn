package Patterns.Adapter;
import java.util.List;
public class NumericalDataAnalyzer implements DataAnalyzer {
    List<Double> data;
    public NumericalDataAnalyzer(){}
    public void setData(List<Double> data) {
        this.data = data;
    }
    @Override
    public double mean() {
        double sum = 0.0;
        for (double item : data) {
            sum += item;
        }
        return sum / data.size();
    }
}

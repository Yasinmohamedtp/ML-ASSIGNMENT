# recommendation_engine.py

def recommend_properties(df, min_area=None, max_price=None, bedrooms=None):
    """
    Recommend properties based on certain criteria like area, price, and number of bedrooms.
    """
    recommendations = df.copy()

    if min_area:
        recommendations = recommendations[recommendations['Area'] >= min_area]
    
    if max_price:
        recommendations = recommendations[recommendations['Price'] <= max_price]
    
    if bedrooms:
        recommendations = recommendations[recommendations['Bedrooms'] == bedrooms]
    
    return recommendations
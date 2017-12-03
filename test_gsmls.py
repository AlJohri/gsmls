import json
import html2text

from gsmls import get_listings, get_listing_detail_preview

def test_gsmls():
    for listing in get_listings('Hudson',
                                min_list_price='350000',
                                max_list_price='500000',
                                min_bedrooms='3',
                                min_bathrooms='2'):
        print(json.dumps(listing))
    last_listing_id = listing['id']
    html = get_listing_detail_preview(last_listing_id)
    print(html2text.html2text(html))

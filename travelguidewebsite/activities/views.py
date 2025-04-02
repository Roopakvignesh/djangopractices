from django.shortcuts import render
activities_data = [ 
    # Goa Beach (id=1) 
    { 
        "id": 1, 
        "destination_id": 1, 
        "name": "Scuba Diving", 
        "image": "https://example.com/scuba.jpg", 
        "description": "Explore the underwater world with expert guides." 
    }, 
    { 
        "id": 2, 
        "destination_id": 1, 
        "name": "Jet Skiing", 
        "image": "https://example.com/jetski.jpg", 
        "description": "Ride the waves and feel the adrenaline rush!" 
    }, 
    { 
        "id": 3, 
        "destination_id": 1, 
        "name": "Beach Volleyball", 
        "image": "https://example.com/volleyball.jpg", 
        "description": "Enjoy an exciting game of volleyball on the beach." 
    }, 
 
    # Manali Hills (id=2) 
    { 
        "id": 4, 
        "destination_id": 2, 
        "name": "Paragliding", 
        "image": "https://example.com/paragliding.jpg", 
        "description": "Soar high above the mountains and enjoy breathtaking views." 
    }, 
    { 
        "id": 5, 
        "destination_id": 2, 
        "name": "Skiing", 
        "image": "https://example.com/skiing.jpg", 
        "description": "Hit the slopes and experience thrilling snow adventures." 
    }, 
 
    # Pyramids of Giza (id=3) 
    { 
        "id": 6, 
        "destination_id": 3, 
        "name": "Camel Ride", 
        "image": "https://example.com/camel.jpg", 
        "description": "Travel across the golden sands like the ancient Egyptians." 
    }, 
    { 
        "id": 7, 
        "destination_id": 3, 
        "name": "Archaeological Tour", 
        "image": "https://example.com/tour.jpg", 
        "description": "Discover the secrets of ancient Egypt with an expert guide." 
    }, 
 
    # Bali Paradise (id=4) 
    { 
        "id": 8, 
        "destination_id": 4, 
        "name": "Surfing", 
        "image": "https://example.com/surfing.jpg", 
        "description": "Catch the best waves in the heart of Bali!" 
    }, 
    { 
        "id": 9, 
        "destination_id": 4, 
        "name": "Island Hopping", 
        "image": "https://example.com/island.jpg", 
        "description": "Explore beautiful islands and hidden beaches." 
    }, 
 
    # Swiss Alps (id=5) 
    { 
        "id": 10, 
        "destination_id": 5, 
        "name": "Snowboarding", 
        "image": "https://example.com/snowboard.jpg", 
        "description": "Glide through snowy peaks with breathtaking views." 
    }, 
    { 
        "id": 11, 
        "destination_id": 5, 
        "name": "Mountain Trekking", 
        "image": "https://example.com/trekking.jpg", 
        "description": "Experience scenic trails and enjoy panoramic views." 
    }, 
 
    # Machu Picchu (id=6) 
    { 
        "id": 12, 
        "destination_id": 6, 
        "name": "Hiking", 
        "image": "https://example.com/hiking.jpg", 
        "description": "Walk the legendary Inca trail to reach the ancient ruins." 
    }, 
    { 
        "id": 13, 
        "destination_id": 6, 
        "name": "Photography Tour", 
        "image": "https://example.com/photo.jpg", 
        "description": "Capture the beauty of Machu Picchu with professional guides." 
    }, 
 
    # Amazon Rainforest (id=7) 
    { 
        "id": 14, 
        "destination_id": 7, 
        "name": "Wildlife Safari", 
        "image": "https://example.com/safari.jpg", 
        "description": "Spot rare animals in their natural habitat." 
    }, 
    { 
        "id": 15, 
        "destination_id": 7, 
        "name": "River Kayaking", 
        "image": "https://example.com/kayaking.jpg", 
        "description": "Paddle through Amazon’s winding rivers and experience nature." 
    }, 
 
    # Great Barrier Reef (id=8) 
    { 
        "id": 16, 
        "destination_id": 8, 
        "name": "Snorkeling", 
        "image": "https://example.com/snorkeling.jpg", 
        "description": "Discover colorful marine life up close." 
    }, 
    { 
        "id": 17, 
        "destination_id": 8, 
        "name": "Glass Bottom Boat Tour", 
        "image": "https://example.com/boat.jpg", 
        "description": "See the reef without getting wet on a guided boat tour." 
    }, 
    { 
        "id": 18, 
        "destination_id": 8, 
        "name": "Underwater Photography", 
        "image": "https://example.com/underwater.jpg", 
        "description": "Capture stunning marine life photos with expert tips." 
    }, 
    { 
        "id": 19, 
        "destination_id": 8, 
        "name": "Dolphin Watching", 
        "image": "https://example.com/dolphins.jpg", 
        "description": "Spot playful dolphins in the crystal-clear waters." 
    }, 
    { 
        "id": 20, 
        "destination_id": 8, 
        "name": "Coral Reef Diving", 
        "image": "https://example.com/coral.jpg", 
        "description": "Dive deep to explore breathtaking coral formations." 
    } 
] 

# Create your views here.
def activities_list(request):
    context={
        'alist':activities_data
    }
    return render(request,'activities_list.html',context)
def activities_details(request,id):
    data=None
    for x in activities_data:
        if x['id']==id:
            data=x
    context={
        'data':data
    }
    return render(request,'activities_details.html',context)
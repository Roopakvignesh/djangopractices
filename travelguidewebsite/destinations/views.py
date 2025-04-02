from django.shortcuts import render
from activities.views import activities_data
destinations_data = [ 
    { 
        "id": 1, 
        "name": "Goa Beach", 
        "location": "India", 
        "type": "Beach", 
        "rating": 4.7, 
        "image": "https://images.pexels.com/photos/88212/pexels-photo-88212.jpeg?cs=srgb&dl=pexels-umaraffan499-88212.jpg&fm=jpg", 
        "description": "Golden sands, lively nightlife, and water sports paradise!" 
    }, 
    { 
        "id": 2, 
        "name": "Manali Hills", 
        "location": "India", 
        "type": "Mountain", 
        "rating": 4.5, 
        "image": "https://t4.ftcdn.net/jpg/02/57/91/21/360_F_257912197_ySuBhefKYPQIZNa3xeGiObLpgYBnH9U5.jpg", 
        "description": "Snow-capped peaks, adventure activities, and serene views." 
    }, 
    { 
        "id": 3, 
        "name": "Pyramids of Giza", 
        "location": "Egypt", 
        "type": "Historical", 
        "rating": 4.9, 
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR1Wav74BtFim0g9TWLRfiMHdxCkE1DV9UvcA&s", 
        "description": "Ancient wonders of the world, full of mystery and grandeur." 
    }, 
    { 
        "id": 4, 
        "name": "Bali Paradise", 
        "location": "Indonesia", 
        "type": "Beach", 
        "rating": 4.8, 
        "image": "https://media.istockphoto.com/id/1186175170/photo/bali-indonesia-traveler-on-tree-house-at-diamond-beach-in-nusa-penida-island.jpg?s=612x612&w=0&k=20&c=d7iUh2kD54b9Uw08Ahj3BjENkoKshIfgHmtN8qJQxBA=", 
        "description": "Lush green landscapes, clear waters, and vibrant culture." 
    }, 
    { 
        "id": 5, 
        "name": "Swiss Alps", 
        "location": "Switzerland", 
        "type": "Mountain", 
        "rating": 4.6, 
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTFj_jPm5UrQtJttUuF8GvSxhNao54nEJwB0Q&s", 
        "description": "Stunning scenery, ski resorts, and breathtaking hikes." 
    }, 
    { 
        "id": 6, 
        "name": "Machu Picchu", 
        "location": "Peru", 
        "type": "Historical", 
        "rating": 4.8, 
        "image": "https://images.unsplash.com/photo-1587595431973-160d0d94add1?fm=jpg&q=60&w=3000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8bWFjaHUlMjBwaWNjaHV8ZW58MHx8MHx8fDA%3D", 
        "description": "Lost city of the Incas, hidden high in the Andes mountains." 
    }, 
    { 
        "id": 7, 
        "name": "Amazon Rainforest", 
        "location": "Brazil", 
        "type": "Adventure", 
        "rating": 4.7, 
        "image": "https://media.istockphoto.com/id/935746242/photo/mata-atlantica-atlantic-forest-in-brazil.jpg?s=612x612&w=0&k=20&c=NqE6m2Q8J2w6M7x7Pi8VxnMzLzq-HJQvCt5EMuvMU5o=", 
        "description": "Explore the world’s largest tropical rainforest filled with wildlife." 
    }, 
    { 
        "id": 8, 
        "name": "Great Barrier Reef", 
        "location": "Australia", 
        "type": "Beach", 
        "rating": 4.9, 
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRWmMZ_-k_4jY65VFXJMk2uuHoNcy7ZMrIXZg&s", 
        "description": "World’s largest coral reef system, a paradise for divers." 
    } 
] 

# Create your views here.
def destination_list(request):
    context={
        'dlist':destinations_data,
        'typelist':['Beach', 'Mountain', 'Historical', 'Adventure'],
    }
    return render(request,'destination_list.html',context)
def destination_details(request,id):
    data=None
    for x in destinations_data:
        if x['id']==id:
            data=x
    context={
        'data':data,
        'activities':activities_data,
    }
    return render(request,'destination_details.html',context)
def index(request):return render(request,'index.html')

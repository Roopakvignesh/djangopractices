from django.shortcuts import render

# Create your views here.
articles_list = [
    {
        "id": 1,
        "name": "The Rise of AI in Healthcare",
        "content": "Artificial Intelligence is revolutionizing healthcare by improving diagnostics, streamlining administrative tasks, and personalizing treatment plans. Machine learning algorithms analyze vast medical data, helping doctors detect diseases early. AI-powered chatbots assist patients, reducing hospital workload. However, ethical concerns like data privacy and bias remain key challenges. The future of AI in healthcare promises better efficiency and improved patient outcomes, provided that regulations ensure fair and transparent use of technology.",
        "author": "Alice Johnson"
    },
    {
        "id": 2,
        "name": "The Future of Remote Work",
        "content": "Remote work has transformed industries, offering employees flexibility and businesses cost savings. Companies are investing in digital tools to enhance collaboration and productivity. However, challenges such as maintaining company culture and preventing burnout persist. Hybrid models, blending remote and in-office work, seem to be the future. As technology evolves, remote work is expected to become more seamless, making location-independent jobs a norm rather than an exception.",
        "author": "John Smith"
    },
    {
        "id": 3,
        "name": "The Impact of Climate Change",
        "content": "Climate change is affecting ecosystems, weather patterns, and global economies. Rising temperatures lead to more extreme weather events such as hurricanes and wildfires. Governments and organizations are investing in renewable energy and sustainable practices to combat these effects. Individuals can contribute by reducing waste, conserving energy, and supporting green initiatives. The fight against climate change requires collective efforts from policymakers, businesses, and citizens worldwide.",
        "author": "Emma Williams"
    },
    {
        "id": 4,
        "name": "Cybersecurity in the Digital Age",
        "content": "With increasing reliance on technology, cybersecurity threats have become more sophisticated. Cyberattacks target personal data, businesses, and even governments. Organizations must implement strong security protocols, such as multi-factor authentication and encryption. Educating users on phishing and social engineering attacks is crucial. As technology advances, cybersecurity will remain a top priority, requiring continuous innovation and vigilance to protect sensitive information.",
        "author": "David Brown"
    },
    {
        "id": 5,
        "name": "The Evolution of Electric Vehicles",
        "content": "Electric vehicles (EVs) are gaining popularity due to their environmental benefits and lower running costs. Advances in battery technology have improved EV range and charging speeds. Governments are offering incentives to encourage adoption. Automakers are investing heavily in EV production, signaling a shift away from traditional fuel-powered cars. As infrastructure improves and costs decrease, EVs will become the dominant mode of transport in the future.",
        "author": "Sophia Martinez"
    },
    {
        "id": 6,
        "name": "The Importance of Mental Health",
        "content": "Mental health is as important as physical health, yet it often goes overlooked. Stress, anxiety, and depression impact millions worldwide. Open conversations, therapy, and self-care practices can help individuals manage their mental well-being. Employers are recognizing the importance of mental health by offering wellness programs and flexible work arrangements. Prioritizing mental health leads to better productivity, relationships, and overall quality of life.",
        "author": "Michael Lee"
    },
    {
        "id": 7,
        "name": "Blockchain Beyond Cryptocurrency",
        "content": "Blockchain technology extends beyond cryptocurrencies, finding applications in supply chain management, digital identity, and secure voting systems. Its decentralized and transparent nature enhances security and trust in various industries. Businesses are exploring blockchain for smart contracts, reducing intermediaries and improving efficiency. As adoption grows, blockchain is set to revolutionize data management and digital transactions worldwide.",
        "author": "Olivia Adams"
    },
    {
        "id": 8,
        "name": "The Role of Space Exploration",
        "content": "Space exploration has led to remarkable technological advancements, from satellite communications to medical innovations. Missions to Mars and beyond aim to uncover the mysteries of the universe. Private companies are joining the space race, making space travel more accessible. While challenges like high costs persist, the benefits of space research, including climate monitoring and resource discovery, make it a crucial endeavor for humanity’s future.",
        "author": "James Carter"
    },
    {
        "id": 9,
        "name": "The Rise of E-Learning",
        "content": "E-learning has transformed education, offering flexible and accessible learning opportunities. Online courses, virtual classrooms, and AI-driven tutoring systems enhance the learning experience. However, challenges like digital divide and student engagement persist. Institutions and educators are adopting innovative methods to improve remote education. As technology advances, e-learning will continue to shape the future of education worldwide.",
        "author": "Emily White"
    },
    {
        "id": 10,
        "name": "The Future of Renewable Energy",
        "content": "Renewable energy sources, such as solar and wind power, are essential for reducing dependence on fossil fuels. Advances in energy storage and grid infrastructure are making renewables more reliable. Governments are investing in sustainable energy projects, aiming to lower carbon emissions. The transition to renewable energy is critical for combating climate change and ensuring a sustainable future for future generations.",
        "author": "Daniel Green"
    }
]

def home(request):
    context={
        'article_list':articles_list

    }
    return render(request,'home.html',context)
def about(request):return render(request,'about.html')
def article_details(request,id):
    data=None
    
    for article in articles_list:
        if article['id']==id:
            data=article
            break
    context={
        'article':data
    }
    return render(request,'article_details.html',context)                                                                                                           
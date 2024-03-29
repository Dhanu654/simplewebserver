# EX01 Developing a Simple Webserver


## AIM:
To develop a simple webserver to serve html pages.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Serving the HTML pages.

### Step 5:
Testing the webserver.

## PROGRAM:
~~~
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH"
      crossorigin="anonymous"
    />
    <link
      rel="stylesheet"
      href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css"
    />
    <style>
      .row1 {
        display: flex;
        background-color: #d5d3cb;
        height: 60px;
        place-items: center;
      }
      .icontop {
        color: #cc324b;
        font-size: 20px;
        padding: 10px;
      }
      a {
        color: #cc324b;
        font-family: "arial";
        text-decoration: none;
        font-size: 18px;
      }
      a:hover {
        color: white;
      }
      .row2 {
        display: flex;
        background-color: white;
        height: 100px;
        place-items: center;
      }
      .row3 {
        display: flex;
        background-color: #d5d3cb;
        place-items: center;
      }
      .row3txt {
        color: white;
        font-family: Arial;
        font-size: 25px;
        padding: 20px;
      }
      .row3btn {
        color: #cc324b;
        background-color: azure;
        margin-left: 20px;
        padding: 20px;
        font-size: 25px;
      }
    </style>
  </head>
  <body>
    <div class="row1">
      <div style="width: 40%">
        <i class="bi bi-twitter icontop"></i>
        <i class="bi bi-youtube icontop"></i>
        <i class="bi bi-facebook icontop"></i>
        <i class="bi bi-whatsapp icontop"></i>
        <i class="bi bi-instagram icontop"></i>
      </div>
      <div style="width: 40%">
        <a href="">Alumni </a>
        <i class="bi bi-three-dots-vertical" style="color: #cc324b"></i>
        <a href="">Events </a>
        <i class="bi bi-three-dots-vertical" style="color: #cc324b"></i>
        <a href="">Career </a>
        <i class="bi bi-three-dots-vertical" style="color: #cc324b"></i>
        <a href="">Login </a>
        <i class="bi bi-three-dots-vertical" style="color: #cc324b"></i>
        <a href="">SEC Portal </a>
      </div>
      <div style="width: 20%">
        <div style="border: 2px solid; border-radius: 20px">
          <i class="bi bi-search"></i>
          <input
            type="text"
            name="search"
            placeholder="Search"
            style="background-color: #d5d3cb; border: 0px"
          />
        </div>
      </div>
    </div>
    <!--Row 2-->
    <div class="row2">
      <div style="width: 35%"><img src="C:\Users\admin\Downloads\logo..png " style="width: 100%" /></div>
      <div style="width: 50%">
        <a href="">Alumni </a>
        <i class="bi bi-three-dots-vertical" style="color: #cc324b"></i>
        <a href="">Events </a>
        <i class="bi bi-three-dots-vertical" style="color: #cc324b"></i>
        <a href="">Career </a>
        <i class="bi bi-three-dots-vertical" style="color: #cc324b"></i>
        <a href="">Login </a>
        <i class="bi bi-three-dots-vertical" style="color: #cc324b"></i>
        <a href="">SEC Portal </a>
      </div>
      <div style="width: 15%; background-color: gray; font-size: 25px">
        Admissions <br /><i class="bi bi-whatsapp"></i> 8939902737
      </div>
    </div>
    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
      crossorigin="anonymous"
    ></script>
    <!--Row 3-->
    <div class="row3">
      <div style="width: 25%; background-color: #cc324b">
        <div class="row3txt">ADMISSION ENQUIRY</div>
        <button class="row3btn">APPLY NOW</button>
        <div class="row3txt">Chat with Student Ambassador</div>
        <button class="row3btn">KNOW MORE</button>
        <div class="row3txt">BLOGS</div>
        <button class="row3btn">KNOW MORE</button>
      </div>

      <div style="width: 75%; padding: 10px">
        <div
          id="carouselExampleIndicators"
          class="carousel slide"
          data-bs-ride="carousel"
        >
          <div class="carousel-indicators">
            <button
              type="button"
              data-bs-target="#carouselExampleIndicators"
              data-bs-slide-to="0"
              class="active"
              aria-current="true"
              aria-label="Slide 1"
            ></button>
            <button
              type="button"
              data-bs-target="#carouselExampleIndicators"
              data-bs-slide-to="1"
              aria-label="Slide 2"
            ></button>
            <button
              type="button"
              data-bs-target="#carouselExampleIndicators"
              data-bs-slide-to="2"
              aria-label="Slide 3"
            ></button>
            
          </div>
          <div class="carousel-inner">
            <div class="carousel-item active">
              <img src="c:\Users\admin\Pictures\Screenshots\Screenshot 2024-03-29 153143.png " class="d-block w-100" alt="..." />
            </div>
            <div class="carousel-item">
              <img src="c:\Users\admin\Pictures\Screenshots\Screenshot 2024-03-29 153206.png " class="d-block w-100" alt="..." />
            </div>
            <div class="carousel-item">
              <img src="c:\Users\admin\Pictures\Screenshots\Screenshot 2024-03-29 153232.png" class="d-block w-100" alt="..." />
            </div>
            
          </div>
          <button
            class="carousel-control-prev"
            type="button"
            data-bs-target="#carouselExampleIndicators"
            data-bs-slide="prev"
          >
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
          </button>
          <button
            class="carousel-control-next"
            type="button"
            data-bs-target="#carouselExampleIndicators"
            data-bs-slide="next"
          >
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
          </button>
        </div>
      </div>
    </div>
  </body>
</html>
</body>
</html>
~~~

## OUTPUT:
![Screenshot 2024-03-29 154007](https://github.com/Dhanu654/simplewebserver/assets/148514965/027a4842-1d38-4e90-b237-ef9817c702fb)




## RESULT:
The program for implementing simple webserver is executed successfully.

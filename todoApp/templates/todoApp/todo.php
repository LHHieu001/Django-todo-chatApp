<head>
    <script src="//d.bablic.com/snippet/6288d4c3c4c5800001a91242.js?version=3.9"></script>
</head>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
<link rel="stylesheet" href= "https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">
<script src= "https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"> </script> 
<script src= "https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"> </script> 
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.min.js" integrity="sha384-QJHtvGhmr9XOIpI6YVutG+2QOK9T+ZnN4kzFN1RtK3zEFEIsxhlmWl5/YESvpZ13" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-fQybjgWLrvvRgtW6bFlB7jaZrFsaBXjsOMm/tB9LTS58ONXgqbR9W8oWht/amnpF" crossorigin="anonymous"></script>

<section class="vh-100" style="background-color: #eee;">
    <div class="container py-5 h-100">
      <div class="row d-flex justify-content-center align-items-center h-100">
        <div class="col col-lg-9 col-xl-7">
          <div class="card rounded-3">
          <a href="{% url 'logout' %}"><button style="background: firebrick; color: white;" type="submit" class="btn btn-success pull-right">Logout</button></a>
            <div class="card-body p-4">
              <h4 class="text-center my-3 pb-3">Hello {{current_user.username}}!</h4>
          
  
              <form method="POST" class="row row-cols-lg-auto g-3 justify-content-center align-items-center mb-4 pb-2">
                {% csrf_token %}
                <div class="col-12">
                  <div class="form-outline">
                    <label for="form1">Name:</label>
                    <input type="text" id="form1" class="form-control" name="content" placeholder="Enter a task here"/>
                    <label for="type">Type:</label>
                    <select id="type" class="form-control" name="type" required>
                        <option value="Shopping">Shopping</option>
                        <option value="Work">Work</option>
                        <option value="Entertain">Entertain</option>
                        <option value="Family">Family</option>
                        <option value="Unknown">Unknown</option>
                    </select>
                    <label for="form2">Deadline:</label>
                    <input type="date" id="form2" class="form-control" name="date" />
                  </div>
                </div>
  
                <div class="col-12">
                  <button type="submit" class="btn btn-primary">Add Task</button>
                </div>
              </form>
              <table class="table mb-4">
                <thead>
                  <tr>
                    <th scope="col">Content</th>
                    <th scope="col">Type</th>
                    <th scope="col">Status</th>
                    <th scope="col">Deadline</th>
                    <th scope="col">Created At</th>
                    <th scope="col">Actions</th>
                  </tr>
                </thead>
                <tbody>
                  {% for i in todos %}
                  <tr>
                    <td>{{i.name}}</td>
                    <td>{{i.type}}</td>
                    {% if i.status == True %}
                      <td style="color: green;">Completed</td>
                    {% else %}
                      <td>In progress</td>
                    {% endif %}
                    <td>{{i.deadline}}</td>
                    <td>{{i.created_at}}</td>

                    <td>
                      <a href="{% url 'delete-todo' i.id %}"><button type="submit" class="btn btn-danger">Delete</button></a>
                      <a href="{% url 'Finished-todo' i.id %}"><button type="submit" class="btn btn-success ms-1">Finished</button></a>
                    </td>
                  </tr>
                  {% endfor %}
                </tbody>
              </table>
  
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

<style>
  .form-control{
    margin-bottom: 5px;
  }
</style>

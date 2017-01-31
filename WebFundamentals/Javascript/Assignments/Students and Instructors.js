var students = [
    {first_name: 'Michael', last_name: 'Jordan'},
    {first_name: 'John', last_name: 'Rosales'},
    {first_name: 'Mark', last_name: 'Guillen'},
    {first_name: 'KB', last_name: 'Tonel'}
]
var users = {
 'Students': [
     {first_name:  'Michael', last_name : 'Jordan'},
     {first_name : 'John', last_name : 'Rosales'},
     {first_name : 'Mark', last_name : 'Guillen'},
     {first_name : 'KB', last_name : 'Tonel'}
  ],
 'Instructors': [
     {first_name : 'Michael', last_name : 'Choi'},
     {first_name : 'Martin', last_name : 'Puryear'}
  ]
 }
console.log(students[0].first_name, students[0].last_name + "\n" + 
students[1].first_name, students[1].last_name + "\n" +
students[2].first_name, students[2].last_name + "\n" +
students[3].first_name, students[3].last_name + "\n");
formatNames(users);

function formatNames(names){
    var nameLength = 0;
    console.log("Students");
    for (var i = 0; i < names.Students.length; i++){
        nameLength = names.Students[i].first_name.length + names.Students[i].last_name.length;
        console.log(i + 1 + " - " + names.Students[i].first_name.toUpperCase() + " " + names.Students[i].last_name.toUpperCase() + " - " + nameLength);
    }
    console.log("Instructors");
    for (var i = 0; i < names.Instructors.length; i++){
        nameLength = names.Instructors[i].first_name.length + names.Instructors[i].last_name.length;
        console.log(i + 1 + " - " + names.Instructors[i].first_name.toUpperCase() + " " + names.Instructors[i].last_name.toUpperCase() + " - " + nameLength);
    }
}

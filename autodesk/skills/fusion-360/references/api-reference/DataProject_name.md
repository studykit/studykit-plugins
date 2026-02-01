# DataProject.name Property

Parent Object: [DataProject](DataProject.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataProject.h>

## Description

Gets and sets the name of the project.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataProject\_var" is a variable referencing a DataProject object. |

"dataProject\_var" is a variable referencing a DataProject object. ```` ``` #include <Core/Dashboard/DataProject.h>  // Get the value of the property. string propertyValue = dataProject_var->name();  // Set the value of the property, where value_var is a string. bool returnValue = dataProject_var->name(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
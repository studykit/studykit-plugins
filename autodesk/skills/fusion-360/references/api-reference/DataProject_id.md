# DataProject.id Property

Parent Object: [DataProject](DataProject.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataProject.h>

## Description

Returns the unique ID for this project. This is the same id used in the APS Data Management API in an unencoded form and will look something like this: "a.45637".

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataProject\_var" is a variable referencing a DataProject object. |

"dataProject\_var" is a variable referencing a DataProject object. ```` ``` #include <Core/Dashboard/DataProject.h>  // Get the value of the property. string propertyValue = dataProject_var->id(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
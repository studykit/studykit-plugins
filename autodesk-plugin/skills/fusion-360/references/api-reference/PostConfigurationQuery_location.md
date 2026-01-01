# PostConfigurationQuery.location Property

Parent Object: [PostConfigurationQuery](PostConfigurationQuery.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Post/PostConfigurationQuery.h>

## Description

The location specifies the location to search in the post library. Setting the location clears any previous specified URL.

## Syntax

* [Python](#Python)
* [C++](#C++)

"postConfigurationQuery\_var" is a variable referencing a PostConfigurationQuery object. |

"postConfigurationQuery\_var" is a variable referencing a PostConfigurationQuery object. ```` ``` #include <Cam/Post/PostConfigurationQuery.h>  // Get the value of the property. LibraryLocations propertyValue = postConfigurationQuery_var->location();  // Set the value of the property, where value_var is a LibraryLocations. bool returnValue = postConfigurationQuery_var->location(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [LibraryLocations](LibraryLocations.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
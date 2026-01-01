# ToolQuery.location Property

Parent Object: [ToolQuery](ToolQuery.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Tools/ToolQuery.h>

## Description

Specifies the location to search in the Tool library. Setting the location clears any previous specified URL. When searching inside a ToolLibrary the location will be ignored.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toolQuery\_var" is a variable referencing a ToolQuery object. |

"toolQuery\_var" is a variable referencing a ToolQuery object. ```` ``` #include <Cam/Tools/ToolQuery.h>  // Get the value of the property. LibraryLocations propertyValue = toolQuery_var->location();  // Set the value of the property, where value_var is a LibraryLocations. bool returnValue = toolQuery_var->location(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [LibraryLocations](LibraryLocations.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
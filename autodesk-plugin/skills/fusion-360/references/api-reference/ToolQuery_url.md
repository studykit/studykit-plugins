# ToolQuery.url Property

Parent Object: [ToolQuery](ToolQuery.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Tools/ToolQuery.h>

## Description

The URL specifies the location and folder to search for in the Tool library. Setting the URL updates the location. When searching inside a ToolLibrary the URL will be ignored.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toolQuery\_var" is a variable referencing a ToolQuery object. |

"toolQuery\_var" is a variable referencing a ToolQuery object. ```` ``` #include <Cam/Tools/ToolQuery.h>  // Get the value of the property. Ptr<URL> propertyValue = toolQuery_var->url();  // Set the value of the property, where value_var is a URL. bool returnValue = toolQuery_var->url(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [URL](URL.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
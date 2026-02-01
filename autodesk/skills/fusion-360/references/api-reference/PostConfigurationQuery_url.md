# PostConfigurationQuery.url Property

Parent Object: [PostConfigurationQuery](PostConfigurationQuery.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Post/PostConfigurationQuery.h>

## Description

The URL specifies the location and folder to search for in the post library. Setting the URL updates the location.

## Syntax

* [Python](#Python)
* [C++](#C++)

"postConfigurationQuery\_var" is a variable referencing a PostConfigurationQuery object. |

"postConfigurationQuery\_var" is a variable referencing a PostConfigurationQuery object. ```` ``` #include <Cam/Post/PostConfigurationQuery.h>  // Get the value of the property. Ptr<URL> propertyValue = postConfigurationQuery_var->url();  // Set the value of the property, where value_var is a URL. bool returnValue = postConfigurationQuery_var->url(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [URL](URL.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
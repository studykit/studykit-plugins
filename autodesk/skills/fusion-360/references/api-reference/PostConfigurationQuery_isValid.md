# PostConfigurationQuery.isValid Property

Parent Object: [PostConfigurationQuery](PostConfigurationQuery.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Post/PostConfigurationQuery.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"postConfigurationQuery\_var" is a variable referencing a PostConfigurationQuery object. |

"postConfigurationQuery\_var" is a variable referencing a PostConfigurationQuery object. ```` ``` #include <Cam/Post/PostConfigurationQuery.h>  // Get the value of the property. boolean propertyValue = postConfigurationQuery_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
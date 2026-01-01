# Application.fontNames Property

Parent Object: [Application](Application.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Application.h>

## Description

Returns the names of all of the fonts that are available in Fusion when creating text.

## Syntax

* [Python](#Python)
* [C++](#C++)

"application\_var" is a variable referencing an Application object. |

"application\_var" is a variable referencing an Application object. ```` ``` #include <Core/Application/Application.h>  // Get the value of the property. std::vector<string> propertyValue = application_var->fontNames(); ``` ```` |

## Property Value

This is a read only property whose value is an array of type string.

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
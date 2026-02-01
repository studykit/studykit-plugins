# NamedViews.count Property

Parent Object: [NamedViews](NamedViews.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/NamedViews.h>

## Description

Returns the number of named views associated with the product. The four standard named views ("TOP", "FRONT", "RIGHT", and "HOME") are not included in this count. Only user-created named view are counted.

## Syntax

* [Python](#Python)
* [C++](#C++)

"namedViews\_var" is a variable referencing a NamedViews object. |

"namedViews\_var" is a variable referencing a NamedViews object. ```` ``` #include <Core/Application/NamedViews.h>  // Get the value of the property. uinteger propertyValue = namedViews_var->count(); ``` ```` |

## Property Value

This is a read only property whose value is a uinteger.

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
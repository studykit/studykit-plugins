# NamedViews.topNamedView Property

Parent Object: [NamedViews](NamedViews.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/NamedViews.h>

## Description

Returns the standard named view called "TOP".

## Syntax

* [Python](#Python)
* [C++](#C++)

"namedViews\_var" is a variable referencing a NamedViews object. |

"namedViews\_var" is a variable referencing a NamedViews object. ```` ``` #include <Core/Application/NamedViews.h>  // Get the value of the property. Ptr<NamedView> propertyValue = namedViews_var->topNamedView(); ``` ```` |

## Property Value

This is a read only property whose value is a [NamedView](NamedView.htm).

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
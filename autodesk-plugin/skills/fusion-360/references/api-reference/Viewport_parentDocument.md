# Viewport.parentDocument Property

Parent Object: [Viewport](Viewport.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Viewport.h>

## Description

Returns the parent document of this viewport.

## Syntax

* [Python](#Python)
* [C++](#C++)

"viewport\_var" is a variable referencing a Viewport object. |

"viewport\_var" is a variable referencing a Viewport object. ```` ``` #include <Core/Application/Viewport.h>  // Get the value of the property. Ptr<Document> propertyValue = viewport_var->parentDocument(); ``` ```` |

## Property Value

This is a read only property whose value is a [Document](Document.htm).

## Version

Introduced in version September 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# BooleanProperty.isReadOnly Property

Parent Object: [BooleanProperty](BooleanProperty.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/BooleanProperty.h>

## Description

Indicates if this property is read-only. If True any attempted edits will fail.

## Syntax

* [Python](#Python)
* [C++](#C++)

"booleanProperty\_var" is a variable referencing a BooleanProperty object. |

"booleanProperty\_var" is a variable referencing a BooleanProperty object. ```` ``` #include <Core/Application/BooleanProperty.h>  // Get the value of the property. boolean propertyValue = booleanProperty_var->isReadOnly(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
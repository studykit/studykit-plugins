# ChoiceProperty.isValid Property

Parent Object: [ChoiceProperty](ChoiceProperty.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/ChoiceProperty.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"choiceProperty\_var" is a variable referencing a ChoiceProperty object. |

"choiceProperty\_var" is a variable referencing a ChoiceProperty object. ```` ``` #include <Core/Application/ChoiceProperty.h>  // Get the value of the property. boolean propertyValue = choiceProperty_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
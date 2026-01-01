# ConstructionAxis.isLightBulbOn Property

Parent Object: [ConstructionAxis](ConstructionAxis.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionAxis.h>

## Description

Indicates if the light bulb (as displayed in the browser) is on. A construction axis will only be visible if it's light bulb, and that of it's containing folder and parent component/s are also on.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionAxis\_var" is a variable referencing a ConstructionAxis object. |

"constructionAxis\_var" is a variable referencing a ConstructionAxis object. ```` ``` #include <Fusion/Construction/ConstructionAxis.h>  // Get the value of the property. boolean propertyValue = constructionAxis_var->isLightBulbOn();  // Set the value of the property, where value_var is a boolean. bool returnValue = constructionAxis_var->isLightBulbOn(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
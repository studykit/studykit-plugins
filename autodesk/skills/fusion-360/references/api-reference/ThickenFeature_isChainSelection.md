# ThickenFeature.isChainSelection Property

Parent Object: [ThickenFeature](ThickenFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ThickenFeature.h>

## Description

Get and sets whether faces that are tangentially connected to the input faces will be included in the thicken feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"thickenFeature\_var" is a variable referencing a ThickenFeature object. |

"thickenFeature\_var" is a variable referencing a ThickenFeature object. ```` ``` #include <Fusion/Features/ThickenFeature.h>  // Get the value of the property. boolean propertyValue = thickenFeature_var->isChainSelection(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# ThreadFeature.hole Property

Parent Object: [ThreadFeature](ThreadFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ThreadFeature.h>

## Description

If this thread feature is was created as the result of creating a tapped hole, this property will return the associated hole feature. If this is a standard thread feature, this property will return null.

## Syntax

* [Python](#Python)
* [C++](#C++)

"threadFeature\_var" is a variable referencing a ThreadFeature object. |

"threadFeature\_var" is a variable referencing a ThreadFeature object. ```` ``` #include <Fusion/Features/ThreadFeature.h>  // Get the value of the property. Ptr<HoleFeature> propertyValue = threadFeature_var->hole(); ``` ```` |

## Property Value

This is a read only property whose value is a [HoleFeature](HoleFeature.htm).

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
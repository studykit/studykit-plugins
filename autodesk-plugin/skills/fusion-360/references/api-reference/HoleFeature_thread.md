# HoleFeature.thread Property

Parent Object: [HoleFeature](HoleFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/HoleFeature.h>

## Description

When a tapped hole is created, a thread feature is also automatically created and controls the tapped threads. The thread feature is tied to the hole and is not displayed in the timeline and is suppressed if the hole is suppressed and deleted if the hole is deleted. This property returns the thread feature associated with this hole if it is a tapped hole. It returns null for all other hole types.

## Syntax

* [Python](#Python)
* [C++](#C++)

"holeFeature\_var" is a variable referencing a HoleFeature object. |

"holeFeature\_var" is a variable referencing a HoleFeature object. ```` ``` #include <Fusion/Features/HoleFeature.h>  // Get the value of the property. Ptr<ThreadFeature> propertyValue = holeFeature_var->thread(); ``` ```` |

## Property Value

This is a read only property whose value is a [ThreadFeature](ThreadFeature.htm).

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
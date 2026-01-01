# RipFeature.definition Property

Parent Object: [RipFeature](RipFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/RipFeature.h>

## Description

Returns the RipFeatureDefinition object which provides access to the information defining this RipFeature and the ability to edit it.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ripFeature\_var" is a variable referencing a RipFeature object. |

"ripFeature\_var" is a variable referencing a RipFeature object. ```` ``` #include <Fusion/SheetMetal/RipFeature.h>  // Get the value of the property. Ptr<RipFeatureDefinition> propertyValue = ripFeature_var->definition(); ``` ```` |

## Property Value

This is a read only property whose value is a [RipFeatureDefinition](RipFeatureDefinition.htm).

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# AlongEdgeRipFeatureDefinition.gapDistance Property

Parent Object: [AlongEdgeRipFeatureDefinition](AlongEdgeRipFeatureDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/AlongEdgeRipFeatureDefinition.h>

## Description

Gets the ModelParameter that defines the gap distance of the rip. The value can be edited by using the properties of the returned ModelParameter object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"alongEdgeRipFeatureDefinition\_var" is a variable referencing an AlongEdgeRipFeatureDefinition object. |

"alongEdgeRipFeatureDefinition\_var" is a variable referencing an AlongEdgeRipFeatureDefinition object. ```` ``` #include <Fusion/SheetMetal/AlongEdgeRipFeatureDefinition.h>  // Get the value of the property. Ptr<ModelParameter> propertyValue = alongEdgeRipFeatureDefinition_var->gapDistance(); ``` ```` |

## Property Value

This is a read only property whose value is a [ModelParameter](ModelParameter.htm).

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
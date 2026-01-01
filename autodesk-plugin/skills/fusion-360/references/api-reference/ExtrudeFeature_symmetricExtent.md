# ExtrudeFeature.symmetricExtent Property

Parent Object: [ExtrudeFeature](ExtrudeFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ExtrudeFeature.h>

## Description

If the current extent of the feature is defined as a symmetric extent, this property returns the SymmericExtentDefinition object that provides access to the information defining the symmetric extent. If the current extent is not symmetric, this property returns null. You can determine the type of extent by using the extentType property.

## Syntax

* [Python](#Python)
* [C++](#C++)

"extrudeFeature\_var" is a variable referencing an ExtrudeFeature object.  ```` ``` # Get the value of the property. propertyValue = extrudeFeature_var.symmetricExtent ``` ```` |

"extrudeFeature\_var" is a variable referencing an ExtrudeFeature object. ```` ``` #include <Fusion/Features/ExtrudeFeature.h>  // Get the value of the property. Ptr<SymmetricExtentDefinition> propertyValue = extrudeFeature_var->symmetricExtent(); ``` ```` |

## Property Value

This is a read only property whose value is a [SymmetricExtentDefinition](SymmetricExtentDefinition.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Extrude Feature API Sample](ExtrudeFeatureSample_Sample.htm) | Demonstrates creating a new extrude feature. |

## Version

Introduced in version March 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# PathPatternFeatures.createInput Method

Parent Object: [PathPatternFeatures](PathPatternFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PathPatternFeatures.h>

## Description

Creates a PathPatternFeatureInput object. Use properties and methods on this object to define the path pattern you want to create and then use the Add method, passing in the PathPatternFeatureInput object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"pathPatternFeatures\_var" is a variable referencing a [PathPatternFeatures](PathPatternFeatures.htm) object.```` ``` returnValue = pathPatternFeatures_var.createInput(inputEntities, path, quantity, distance, patternDistanceType) ``` ```` |

"pathPatternFeatures\_var" is a variable referencing a [PathPatternFeatures](PathPatternFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [PathPatternFeatureInput](PathPatternFeatureInput.htm) | Returns the newly created PathPatternFeatureInput object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputEntities | [ObjectCollection](ObjectCollection.htm) | The collection can contain faces, features, bodies or occurrences. All of the entities must be of a single type. For example, it can't contain features and occurrences but only features or occurrences. |
| path | [Path](Path.htm) | The Path object that represents a single set of connected curves along which to drive the pattern. |
| quantity | [ValueInput](ValueInput.htm) | Specifies the number of instances in the first direction. |
| distance | [ValueInput](ValueInput.htm) | Specifies the distance. How this value is used depends on the value of the PatternDistanceType property. A negative value can be used to change the direction. If the value is ExtentPatternDistanceType then it defines the total distance of the pattern. If the value is SpacingPatternDistanceType then it defines the distance between each element. |
| patternDistanceType | [PatternDistanceType](PatternDistanceType.htm) | Specifies how the distance between elements is computed. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [pathPatternFeatures.add](pathPatternFeatures_add_Sample.htm) | Demonstrates the pathPatternFeatures.add method using a selected body and sketch curve as the path. |

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
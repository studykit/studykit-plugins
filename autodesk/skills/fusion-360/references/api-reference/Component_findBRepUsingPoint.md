# Component.findBRepUsingPoint Method

Parent Object: [Component](Component.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Component.h>

## Description

Finds all the entities of the specified type at the specified location.

## Syntax

* [Python](#Python)
* [C++](#C++)

"component\_var" is a variable referencing a [Component](Component.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"component\_var" is a variable referencing a [Component](Component.htm) object.  ```` ``` #include <Fusion/Components/Component.h>  // Uses no optional arguments. returnValue = component_var->findBRepUsingPoint(point, entityType);  // Uses optional arguments. returnValue = component_var->findBRepUsingPoint(point, entityType, proximityTolerance, visibleEntitiesOnly); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ObjectCollection](ObjectCollection.htm) | Returns an ObjectCollection containing the entities found. The returned collection can be empty indicating nothing was found. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| point | [Point3D](Point3D.htm) | Input coordinate that specifies the component space point at which to find the entities. |
| entityType | [BRepEntityTypes](BRepEntityTypes.htm) | The type of B-Rep entity wanted. You can also take advantage of B-Rep topology to infer other that other entities were found. For example, If you get a BRepEdge it implies that the faces the edge connects were also found. If a BRepVertex is returned it implies the edges that the vertex connects were found and the faces that the edges connect were found. |
| proximityTolerance | double | Specifies the tolerance for the search. All entities within this distance from the search point that match the filter will be returned. If not specified a default tolerance is used.   This is an optional argument whose default value is -1.0. |
| visibleEntitiesOnly | boolean | indicates whether or not invisible objects should be included in the search. Defaults to True indicating that invisible objects will be ignored.   This is an optional argument whose default value is True. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Hole and Pocket Recognition API Sample](HoleAndPocketRecognition_Sample.htm) | This sample script demonstrates three different methods for feature recognition: one for holes and two for pockets.  The script starts by creating a simple component which is then used to demonstrate the three methods. After the features are recognised they are coloured and milling and drilling operations are created for each feature.  RecognizedHoleGroup returns a list of BRepFaces that can be used as selections for the drilling operation. RecognizedPocket also return some BRepFaces but it needs additional processing before the output can be used for creating machining operations.  The sample script demonstrates a couple of different methods, including finding the pocket BRepFaces and creating sketches from the recognized pockets.  This script works only if the Manufacturing Extension is active. |

## Version

Introduced in version December 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
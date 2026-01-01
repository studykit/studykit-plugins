# BaseComponent.findBRepUsingPoint Method

Parent Object: [BaseComponent](BaseComponent.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/BaseComponent.h>

## Description

Finds all the entities of the specified type at the specified location.

## Syntax

* [Python](#Python)
* [C++](#C++)

"baseComponent\_var" is a variable referencing a [BaseComponent](BaseComponent.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"baseComponent\_var" is a variable referencing a [BaseComponent](BaseComponent.htm) object.  ```` ``` #include <Fusion/Components/BaseComponent.h>  // Uses no optional arguments. returnValue = baseComponent_var->findBRepUsingPoint(point, entityType);  // Uses optional arguments. returnValue = baseComponent_var->findBRepUsingPoint(point, entityType, proximityTolerance, visibleEntitiesOnly); ``` ```` |

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

## Version

Introduced in version December 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
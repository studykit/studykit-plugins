# SweepFeatures.createInputForSolid Method

Parent Object: [SweepFeatures](SweepFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SweepFeatures.h>

## Description

Creates a SweepFeatureInput object for defining a simple sweep feature from a B-Rep solid with a path. Use properties and methods on this object to define the sweep you want to create, and then use the Add method, passing in the SweepFeatureInput object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sweepFeatures\_var" is a variable referencing a [SweepFeatures](SweepFeatures.htm) object.```` ``` returnValue = sweepFeatures_var.createInputForSolid(solidBody, path, operation) ``` ```` |

"sweepFeatures\_var" is a variable referencing a [SweepFeatures](SweepFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SweepFeatureInput](SweepFeatureInput.htm) | Returns the newly created SweepFeatureInput object or null if the creation fails. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| solidBody | [BRepBody](BRepBody.htm) | The BRepBody object to sweep. It must be a solid body. |
| path | [Path](Path.htm) | The Path object that defines the path the body will be swept along. |
| operation | [FeatureOperations](FeatureOperations.htm) | The type of feature operation to perform. |

## Version

Introduced in version May 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# ImportManager.importToTarget Method

Parent Object: [ImportManager](ImportManager.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/ImportManager.h>

## Description

Executes the import operation to import a file (of the format specified by the input ImportOptions object) into an existing component in an existing design.

## Remarks

There is currently a limitation with this method where it cannot be used within any of the Command related events.

## Syntax

* [Python](#Python)
* [C++](#C++)

"importManager\_var" is a variable referencing an [ImportManager](ImportManager.htm) object.```` ``` returnValue = importManager_var.importToTarget(importOptions, target) ``` ```` |

"importManager\_var" is a variable referencing an [ImportManager](ImportManager.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the import was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| importOptions | [ImportOptions](ImportOptions.htm) | An ImportOptions object that is created using one of the create methods on the ImportManager object. This defines the type of file and any available options supported for that file type. Supplying a DXF2DImportOptions object will result in the creation of one or more sketches (depending on the layers in the DXF file) in the target component. |
| target | [Base](Base.htm) | For most import types this will be a Component. For SVGImportOptions this is the sketch you want to import the SVG data into. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Import Manager API Sample](ImportManager_Sample.htm) | Demonstrates how to import different formats to Fusion document |

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
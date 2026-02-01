# ImportManager.createSVGImportOptions Method

Parent Object: [ImportManager](ImportManager.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/ImportManager.h>

## Description

Creates a SVGImportOptions object that is used to import SVG data into a sketch. Creation of the SVGImportOptions object does not perform the import. You must pass this object to the importToTarget or importToTarget2 methods to perform the import and provide the sketch you want to import to as the target.

## Syntax

* [Python](#Python)
* [C++](#C++)

"importManager\_var" is a variable referencing an [ImportManager](ImportManager.htm) object.```` ``` returnValue = importManager_var.createSVGImportOptions(fullFilename) ``` ```` |

"importManager\_var" is a variable referencing an [ImportManager](ImportManager.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SVGImportOptions](SVGImportOptions.htm) | The created SVGImportOptions object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| fullFilename | string | The full filename, including the path, of the SVG file. |

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
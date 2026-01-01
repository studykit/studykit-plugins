# MeshBodies.add Method

Parent Object: [MeshBodies](MeshBodies.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshBody/MeshBodies.h>

## Description

Creates a new mesh body by importing an STL, OBJ or 3MF file.

## Syntax

* [Python](#Python)
* [C++](#C++)

"meshBodies\_var" is a variable referencing a [MeshBodies](MeshBodies.htm) object.```` ``` # Uses no optional arguments. returnValue = meshBodies_var.add(fullFilename, units)  # Uses optional arguments. returnValue = meshBodies_var.add(fullFilename, units, baseOrFormFeature) ``` ```` |

"meshBodies\_var" is a variable referencing a [MeshBodies](MeshBodies.htm) object.  ```` ``` #include <Fusion/MeshBody/MeshBodies.h>  // Uses no optional arguments. returnValue = meshBodies_var->add(fullFilename, units);  // Uses optional arguments. returnValue = meshBodies_var->add(fullFilename, units, baseOrFormFeature); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [MeshBodyList](MeshBodyList.htm) | Returns a list of the newly created mesh bodies or null if the creation failed. Multiple bodies can be created in the case where a .obj file that contains multiple bodies was imported. STL files always contain a single body. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| fullFilename | string | The full filename (path and file) of a STL, OBJ or 3MF file. |
| units | [MeshUnits](MeshUnits.htm) | The units to use when importing the file. |
| baseOrFormFeature | [Base](Base.htm) | The BaseFeature or FormFeature object that this mesh body will be associated with. This is an optional requirement. It is required in a parametric modeling design but is ignored in a direct modeling design.   This is an optional argument whose default value is null. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
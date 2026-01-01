# OBJExportOptions.meshRefinement Property

Parent Object: [OBJExportOptions](OBJExportOptions.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/OBJExportOptions.h>

## Description

Gets and sets the current simple mesh refinement settings. Setting this property will reset the surfaceDeviation, normalDeviation, maximumEdgeLength, and aspectRatio to values that correspond to the specified mesh refinement. The default is MeshRefinementMedium.

## Syntax

* [Python](#Python)
* [C++](#C++)

"oBJExportOptions\_var" is a variable referencing an OBJExportOptions object. |

"oBJExportOptions\_var" is a variable referencing an OBJExportOptions object. ```` ``` #include <Fusion/Fusion/OBJExportOptions.h>  // Get the value of the property. MeshRefinementSettings propertyValue = oBJExportOptions_var->meshRefinement();  // Set the value of the property, where value_var is a MeshRefinementSettings. bool returnValue = oBJExportOptions_var->meshRefinement(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [MeshRefinementSettings](MeshRefinementSettings.htm).

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
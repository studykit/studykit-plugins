# C3MFExportOptions.meshRefinement Property

Parent Object: [C3MFExportOptions](C3MFExportOptions.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/C3MFExportOptions.h>

## Description

Gets and sets the current simple mesh refinement settings. Setting this property will reset the surfaceDeviation, normalDeviation, maximumEdgeLength, and aspectRatio to values that correspond to the specified mesh refinement. The default is MeshRefinementMedium.

## Syntax

* [Python](#Python)
* [C++](#C++)

"c3MFExportOptions\_var" is a variable referencing a C3MFExportOptions object. |

"c3MFExportOptions\_var" is a variable referencing a C3MFExportOptions object. ```` ``` #include <Fusion/Fusion/C3MFExportOptions.h>  // Get the value of the property. MeshRefinementSettings propertyValue = c3MFExportOptions_var->meshRefinement();  // Set the value of the property, where value_var is a MeshRefinementSettings. bool returnValue = c3MFExportOptions_var->meshRefinement(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [MeshRefinementSettings](MeshRefinementSettings.htm).

## Version

Introduced in version September 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
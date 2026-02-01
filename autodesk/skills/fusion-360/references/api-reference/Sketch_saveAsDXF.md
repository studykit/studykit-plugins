# Sketch.saveAsDXF Method

Parent Object: [Sketch](Sketch.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/Sketch.h>

## Description

This function is retired. See more information in the 'Remarks' section below.

## Remarks

This method has been replaced by using the ExportManager.createDXFSketchExportOptions method, which provides additional capabilities.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketch\_var" is a variable referencing a [Sketch](Sketch.htm) object.```` ``` returnValue = sketch_var.saveAsDXF(fullFilename) ``` ```` |

"sketch\_var" is a variable referencing a [Sketch](Sketch.htm) object.  ```` ``` #include <Fusion/Sketch/Sketch.h>  returnValue = sketch_var->saveAsDXF(fullFilename); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the operation was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| fullFilename | string | The full filename, including the path, of the DXF file. |

## Version

Introduced in version August 2014
Retired in version July 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
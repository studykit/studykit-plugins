# NCProgram.fusionHubFolder Property

Parent Object: [NCProgram](NCProgram.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/NCProgram/NCProgram.h>

## Description

Gets and sets the DataFolder to which the exported files should be uploaded to if the parameter nc\_program\_postToFusionTeam is set to true. When a DataFolder is set, nc\_program\_postToFusionTeam is automatically set to true. An exception will be thrown if the DataFolder to set is not valid or not accessible. Depending on the FusionHubExecutionBehaviors used for the export the design may be saved at this location as well.

## Syntax

* [Python](#Python)
* [C++](#C++)

"nCProgram\_var" is a variable referencing a NCProgram object. |

"nCProgram\_var" is a variable referencing a NCProgram object. ```` ``` #include <Cam/NCProgram/NCProgram.h>  // Get the value of the property. Ptr<DataFolder> propertyValue = nCProgram_var->fusionHubFolder();  // Set the value of the property, where value_var is a DataFolder. bool returnValue = nCProgram_var->fusionHubFolder(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [DataFolder](DataFolder.htm).

## Version

Introduced in version July 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
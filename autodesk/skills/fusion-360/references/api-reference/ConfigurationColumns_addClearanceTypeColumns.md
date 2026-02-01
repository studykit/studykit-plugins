# ConfigurationColumns.addClearanceTypeColumns Method

Parent Object: [ConfigurationColumns](ConfigurationColumns.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationColumns.h>

## Description

Creates the columns in the configuration table to control the clearance information associated with a clearance hole. Because configuring a clearance hole requires several pieces of related information, this method collects it all at once and creates all the corresponding feature aspect columns.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationColumns\_var" is a variable referencing a [ConfigurationColumns](ConfigurationColumns.htm) object.```` ``` returnValue = configurationColumns_var.addClearanceTypeColumns(holeFeature, holeClearanceColumns) ``` ```` |

"configurationColumns\_var" is a variable referencing a [ConfigurationColumns](ConfigurationColumns.htm) object.  ```` ``` #include <Fusion/Configurations/ConfigurationColumns.h>  returnValue = configurationColumns_var->addClearanceTypeColumns(holeFeature, holeClearanceColumns); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ConfigurationFeatureAspectColumn](ConfigurationFeatureAspectColumn.htm)[] | Returns an array of the columns created. They are in order of standard, fastener type, and size. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| holeFeature | [HoleFeature](HoleFeature.htm) | The hole feature that defines a clearance hole whose clearance will be controlled by the configuration table. |
| holeClearanceColumns | [ConfigurationClearanceHoleColumns](ConfigurationClearanceHoleColumns.htm) | Enum value that indicates which columns should be created to control the clearance hole definition. You can fully define the clearance hole by specifying the standard, fastener type, and size. Or you can leave the standard controlled by the hole and only configure the fastener type, and size. Or you can leave the standard and fastener type controlled by the hole and only configure the size. As a result, this can create and return 3, 2, or 1 columns.   The fit is also a setting that controls the hole clearance, but it's independent of the other settings and can be created independently using the addFeatureAspectColumn method. |

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
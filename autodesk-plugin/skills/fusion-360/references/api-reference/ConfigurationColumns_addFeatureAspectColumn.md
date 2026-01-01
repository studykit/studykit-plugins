# ConfigurationColumns.addFeatureAspectColumn Method

Parent Object: [ConfigurationColumns](ConfigurationColumns.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationColumns.h>

## Description

Creates a new column to control an aspect of a feature that supports being configured.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationColumns\_var" is a variable referencing a [ConfigurationColumns](ConfigurationColumns.htm) object.```` ``` returnValue = configurationColumns_var.addFeatureAspectColumn(feature, aspectType) ``` ```` |

"configurationColumns\_var" is a variable referencing a [ConfigurationColumns](ConfigurationColumns.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ConfigurationFeatureAspectColumn](ConfigurationFeatureAspectColumn.htm) | Retruns the created ConfigurationFeatureAspectColumn or null in the case of failure. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| feature | [Base](Base.htm) | The feature to be configured. The term "feature" is used broadly and includes ThreadFeature, HoleFeature that is tapped, Joint, and AsBuiltJoint objects. The existing column is returned if a feature aspect column already exists for the feature and aspect type. |
| aspectType | [ConfigurationFeatureAspectTypes](ConfigurationFeatureAspectTypes.htm) | The aspect type to create a column for. The type specified must be a valid type for the specified feature; otherwise, this will fail with an error. |

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# ConfigurationFeatureAspectColumn Object

Derived from: [ConfigurationColumn](ConfigurationColumn.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationFeatureAspectColumn.h>

## Description

Represents a feature aspect column in a configuration table. Feature aspects are properties of a feature that are unique to a particular type of feature. This includes various thread and joint settings.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ConfigurationFeatureAspectColumn_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [deleteMe](ConfigurationFeatureAspectColumn_deleteMe.htm) | Deletes this column from the table. Property columns cannot be deleted. If the table was obtained from a DataFile, this method will fail. |
| [getCell](ConfigurationFeatureAspectColumn_getCell.htm) | Gets the cell in this column at the specified row. Depending on the type of data in the cells within the column a ConfigurationFeatureAspectBooleanCell or ConfigurationFeatureAspectStringCell will be returned. The first row has an index of 0 and does not include the header row. |
| [getCellByRowId](ConfigurationFeatureAspectColumn_getCellByRowId.htm) | This method returns the cell in this column at the row identified by its ID. Depending on the type of data in the cells within the column, a ConfigurationFeatureAspectBooleanCell or ConfigurationFeatureAspectStringCell will be returned. |
| [getCellByRowName](ConfigurationFeatureAspectColumn_getCellByRowName.htm) | Gets the cell in this column at the row specified by its name. Depending on the type of data in the cells within the column a ConfigurationFeatureAspectBooleanCell or ConfigurationFeatureAspectStringCell will be returned. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [aspectType](ConfigurationFeatureAspectColumn_aspectType.htm) | Gets the type of feature aspect this column is controlling. |
| [feature](ConfigurationFeatureAspectColumn_feature.htm) | Returns the feature being controlled by this column. |
| [id](ConfigurationFeatureAspectColumn_id.htm) | The id of the column. This is constant and cannot be changed by the user. |
| [index](ConfigurationFeatureAspectColumn_index.htm) | The index position of this column within the table. The first column is at index 0 and does not include the "Name" column. |
| [isValid](ConfigurationFeatureAspectColumn_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ConfigurationFeatureAspectColumn_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [parentTable](ConfigurationFeatureAspectColumn_parentTable.htm) | This property returns the parent table, either the top or custom theme table this column is in. |
| [rowCount](ConfigurationFeatureAspectColumn_rowCount.htm) | Returns the number of rows in this column. |
| [title](ConfigurationFeatureAspectColumn_title.htm) | The title of this column. In a top table, this can only be edited for suppression, visibility, parameter, and theme table columns. It behaves as read-only for all other types. In a theme table, the title of all the columns can be modified except for the column that represents the root component for materials and appearances.   If the table was obtained from a DataFile, this property behaves as read-only for all the columns. |

## Accessed From

[ConfigurationColumns.addClearanceTypeColumns](ConfigurationColumns_addClearanceTypeColumns.htm), [ConfigurationColumns.addFeatureAspectColumn](ConfigurationColumns_addFeatureAspectColumn.htm), [ConfigurationColumns.addThreadTypeColumns](ConfigurationColumns_addThreadTypeColumns.htm), [ConfigurationFeatureAspectBooleanCell.parentColumn](ConfigurationFeatureAspectBooleanCell_parentColumn.htm), [ConfigurationFeatureAspectStringCell.parentColumn](ConfigurationFeatureAspectStringCell_parentColumn.htm)

## Derived Classes

[ConfigurationJointSnapColumn](ConfigurationJointSnapColumn.htm)

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
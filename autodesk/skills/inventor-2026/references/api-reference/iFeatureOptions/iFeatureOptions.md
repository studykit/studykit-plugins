# iFeatureOptions Object

## Description

The iFeatureOptions object provides access to properties that provide read and write access of the iFeature related application options. This is somewhat equivalent to the iFeature tab of the Application Options dialog.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../iFeatureOptions/iFeatureOptions_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [RootPath](../iFeatureOptions/iFeatureOptions_RootPath.md) | Gets/Sets the location of iFeature files used by the View Catalog dialog box. |
| [SheetMetalPunchesRootPath](../iFeatureOptions/iFeatureOptions_SheetMetalPunchesRootPath.md) | Gets/Sets the location of iFeature files used by the sheet metal Punch Tool dialog box. |
| [Type](../iFeatureOptions/iFeatureOptions_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UseKey1AsBrowserNameColumn](../iFeatureOptions/iFeatureOptions_UseKey1AsBrowserNameColumn.md) | Gets/Sets whether to use the Key 1 column of a table-driven iFeature as the Browser Name column. |
| [UserRootPath](../iFeatureOptions/iFeatureOptions_UserRootPath.md) | Gets/Sets the location of iFeature files used by both the Create iFeature and Insert iFeature dialog boxes. |
| [Viewer](../iFeatureOptions/iFeatureOptions_Viewer.md) | Gets/sets the viewer application used to manage the iFeature files. |
| [ViewerArguments](../iFeatureOptions/iFeatureOptions_ViewerArguments.md) | Gets/Sets the viewer command line arguments for run-time options. |

## Accessed From

[Application.iFeatureOptions](../Application/Application_iFeatureOptions.md), [InventorServer.iFeatureOptions](InventorServer_iFeatureOptions.md), [InventorServerObject.iFeatureOptions](InventorServerObject_iFeatureOptions.md)

## Version

Introduced in version 11

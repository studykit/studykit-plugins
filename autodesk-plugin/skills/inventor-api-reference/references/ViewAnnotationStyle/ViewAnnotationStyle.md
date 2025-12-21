# ViewAnnotationStyle Object

Derived from: [Style](../Style/Style.md) Object

## Description

ViewAnnotationStyle object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [ConvertToLocal](../ViewAnnotationStyle/ViewAnnotationStyle_ConvertToLocal.md) | Method that creates a local cached copy of a global style and returns the local style. |
| [Copy](../ViewAnnotationStyle/ViewAnnotationStyle_Copy.md) | Method that creates a new local Style object. The newly created style is returned. |
| [Delete](../ViewAnnotationStyle/ViewAnnotationStyle_Delete.md) | Method that deletes the Style/Layer/UnfoldMethod. |
| [GetReferenceKey](../ViewAnnotationStyle/ViewAnnotationStyle_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [SaveToGlobal](../ViewAnnotationStyle/ViewAnnotationStyle_SaveToGlobal.md) | Method that saves this style to the global repository. If a style with the same name is found in the repository, that style is updated. |
| [UpdateFromGlobal](../ViewAnnotationStyle/ViewAnnotationStyle_UpdateFromGlobal.md) | Method that updates this style from the global repository. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ViewAnnotationStyle/ViewAnnotationStyle_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Comments](../ViewAnnotationStyle/ViewAnnotationStyle_Comments.md) | Gets and sets comments associated with the style. |
| [CropViewAnnotationSettings](../ViewAnnotationStyle/ViewAnnotationStyle_CropViewAnnotationSettings.md) | Read-only property that returns the CropViewAnnotationStyleSettings object. |
| [InternalName](../ViewAnnotationStyle/ViewAnnotationStyle_InternalName.md) | Property that returns the internal name of the style. The name is the internal English name of the standard style. This name will remain constant and is not affected by locale. This name is never displayed to the user. Note that this name is not guaranteed to be unique. |
| [InUse](../ViewAnnotationStyle/ViewAnnotationStyle_InUse.md) | Property that indicates if this style is in use. |
| [Name](../ViewAnnotationStyle/ViewAnnotationStyle_Name.md) | Gets/Sets the name of the Style. |
| [Parent](../ViewAnnotationStyle/ViewAnnotationStyle_Parent.md) | Property returning the parent of this object. |
| [StyleLocation](../ViewAnnotationStyle/ViewAnnotationStyle_StyleLocation.md) | Property that returns the location of this style, i.e. local to the document, cached locally in the document, exists in the library. Styles that exist in the library cannot be edited. |
| [StyleType](../ViewAnnotationStyle/ViewAnnotationStyle_StyleType.md) | Gets the type of the style. |
| [Type](../ViewAnnotationStyle/ViewAnnotationStyle_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UpToDate](../ViewAnnotationStyle/ViewAnnotationStyle_UpToDate.md) | Property that gets the up-to-date status of the style against the global repository. |

## Accessed From

[CropOperation.Style](../CropOperation/CropOperation_Style.md), [DrawingViewAnnotation.Style](../DrawingViewAnnotation/DrawingViewAnnotation_Style.md), [ObjectDefaultsStyle.AuxiliaryViewLineStyle](../ObjectDefaultsStyle/ObjectDefaultsStyle_AuxiliaryViewLineStyle.md), [ObjectDefaultsStyle.CropCutLineStyle](../ObjectDefaultsStyle/ObjectDefaultsStyle_CropCutLineStyle.md), [ObjectDefaultsStyle.DetailViewCalloutStyle](../ObjectDefaultsStyle/ObjectDefaultsStyle_DetailViewCalloutStyle.md), [ObjectDefaultsStyle.SectionViewLineStyle](../ObjectDefaultsStyle/ObjectDefaultsStyle_SectionViewLineStyle.md), [ViewAnnotationStylesEnumerator.Item](../ViewAnnotationStylesEnumerator/ViewAnnotationStylesEnumerator_Item.md)

## Version

Introduced in version 2025.1

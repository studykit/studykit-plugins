# CentermarkStyle Object

Derived from: [Style](../Style/Style.md) Object

## Description

The CentermarkStyle object represents a center mark style in a drawing.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [ConvertToLocal](../CentermarkStyle/CentermarkStyle_ConvertToLocal.md) | Method that creates a local cached copy of a global style and returns the local style. |
| [Copy](../CentermarkStyle/CentermarkStyle_Copy.md) | Method that creates a new local Style object. The newly created style is returned. |
| [Delete](../CentermarkStyle/CentermarkStyle_Delete.md) | Method that deletes the Style/Layer/UnfoldMethod. |
| [GetReferenceKey](../CentermarkStyle/CentermarkStyle_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [SaveToGlobal](../CentermarkStyle/CentermarkStyle_SaveToGlobal.md) | Method that saves this style to the global repository. If a style with the same name is found in the repository, that style is updated. |
| [UpdateFromGlobal](../CentermarkStyle/CentermarkStyle_UpdateFromGlobal.md) | Method that updates this style from the global repository. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../CentermarkStyle/CentermarkStyle_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Comments](../CentermarkStyle/CentermarkStyle_Comments.md) | Gets and sets comments associated with the style. |
| [DefaultRadius](../CentermarkStyle/CentermarkStyle_DefaultRadius.md) | Gets and sets the size of a sick center mark if it is left detached from geometry. |
| [ExtensionLength](../CentermarkStyle/CentermarkStyle_ExtensionLength.md) | Gets and sets the minimum length of center mark extension lines. |
| [GapDistance](../CentermarkStyle/CentermarkStyle_GapDistance.md) | Gets and sets the gap distance between the center indicator and the extension line. |
| [InternalName](../CentermarkStyle/CentermarkStyle_InternalName.md) | Property that returns the internal name of the style. The name is the internal English name of the standard style. This name will remain constant and is not affected by locale. This name is never displayed to the user. Note that this name is not guaranteed to be unique. |
| [InUse](../CentermarkStyle/CentermarkStyle_InUse.md) | Property that indicates if this style is in use. |
| [MarkSize](../CentermarkStyle/CentermarkStyle_MarkSize.md) | Gets and sets the size of the center indicator mark. |
| [Name](../CentermarkStyle/CentermarkStyle_Name.md) | Gets/Sets the name of the Style. |
| [OvershootDistance](../CentermarkStyle/CentermarkStyle_OvershootDistance.md) | Gets and sets the distance that center mark extension lines extend beyond the edges of the features that they define. |
| [Parent](../CentermarkStyle/CentermarkStyle_Parent.md) | Property returning the parent of this object. |
| [StyleLocation](../CentermarkStyle/CentermarkStyle_StyleLocation.md) | Property that returns the location of this style, i.e. local to the document, cached locally in the document, exists in the library. Styles that exist in the library cannot be edited. |
| [StyleType](../CentermarkStyle/CentermarkStyle_StyleType.md) | Gets the type of the style. |
| [Type](../CentermarkStyle/CentermarkStyle_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UpToDate](../CentermarkStyle/CentermarkStyle_UpToDate.md) | Property that gets the up-to-date status of the style against the global repository. |

## Accessed From

[Centerline.Style](../Centerline/Centerline_Style.md), [Centermark.Style](../Centermark/Centermark_Style.md), [CentermarkStylesEnumerator.Item](../CentermarkStylesEnumerator/CentermarkStylesEnumerator_Item.md), [ObjectDefaultsStyle.CenterlineStyle](../ObjectDefaultsStyle/ObjectDefaultsStyle_CenterlineStyle.md), [ObjectDefaultsStyle.CentermarkStyle](../ObjectDefaultsStyle/ObjectDefaultsStyle_CentermarkStyle.md), [ObjectDefaultsStyle.CenterOfGravityStyle](../ObjectDefaultsStyle/ObjectDefaultsStyle_CenterOfGravityStyle.md), [ObjectDefaultsStyle.SheetMetalPunchStyle](../ObjectDefaultsStyle/ObjectDefaultsStyle_SheetMetalPunchStyle.md), [ObjectDefaultsStyle.WorkAxisStyle](../ObjectDefaultsStyle/ObjectDefaultsStyle_WorkAxisStyle.md), [ObjectDefaultsStyle.WorkPlaneStyle](../ObjectDefaultsStyle/ObjectDefaultsStyle_WorkPlaneStyle.md), [ObjectDefaultsStyle.WorkPointStyle](../ObjectDefaultsStyle/ObjectDefaultsStyle_WorkPointStyle.md)

## Version

Introduced in version 2010

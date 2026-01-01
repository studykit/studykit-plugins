# BalloonStyle Object

Derived from: [Style](../Style/Style.md) Object

## Description

The BalloonStyle object represents a balloon style in a drawing. The properties and methods listed below are in addition to those supported by the Style object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [ConvertToLocal](../BalloonStyle/BalloonStyle_ConvertToLocal.md) | Method that creates a local cached copy of a global style and returns the local style. |
| [Copy](../BalloonStyle/BalloonStyle_Copy.md) | Method that creates a new local Style object. The newly created style is returned. |
| [Delete](../BalloonStyle/BalloonStyle_Delete.md) | Method that deletes the Style/Layer/UnfoldMethod. |
| [GetReferenceKey](../BalloonStyle/BalloonStyle_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [SaveToGlobal](../BalloonStyle/BalloonStyle_SaveToGlobal.md) | Method that saves this style to the global repository. If a style with the same name is found in the repository, that style is updated. |
| [UpdateFromGlobal](../BalloonStyle/BalloonStyle_UpdateFromGlobal.md) | Method that updates this style from the global repository. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AlternateLeaderStyle](../BalloonStyle/BalloonStyle_AlternateLeaderStyle.md) | Property that gets and sets the alternate leader style used for the balloon style. Alternate leader style is used when a balloon termination is dragged away from its associative edge. |
| [Application](../BalloonStyle/BalloonStyle_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [BalloonDiameter](../BalloonStyle/BalloonStyle_BalloonDiameter.md) | Property that gets and sets the balloon diameter. This value is used only if the ScaleToTextHeight property is set to False. This property is not applicable if the balloon type is kNoneBalloonType or kLinearBalloonType. |
| [BalloonType](../BalloonStyle/BalloonStyle_BalloonType.md) | Property that gets and sets the shape of the balloon. Valid types are kCircularWithOneEntryBalloonType, kCircularWithTwoEntriesBalloonType, kHexagonBalloonType, kLinearBalloonType and kNoneBalloonType. |
| [Comments](../BalloonStyle/BalloonStyle_Comments.md) | Gets and sets comments associated with the style. |
| [DefaultOffset](../BalloonStyle/BalloonStyle_DefaultOffset.md) | Property that gets and sets the default distance between balloons when they are aligned. Changing this value has no effect on previously created balloons. |
| [InternalName](../BalloonStyle/BalloonStyle_InternalName.md) | Property that returns the internal name of the style. The name is the internal English name of the standard style. This name will remain constant and is not affected by locale. This name is never displayed to the user. Note that this name is not guaranteed to be unique. |
| [InUse](../BalloonStyle/BalloonStyle_InUse.md) | Property that indicates if this style is in use. |
| [LeaderStyle](../BalloonStyle/BalloonStyle_LeaderStyle.md) | Property that gets and sets the leader style used for a balloon. |
| [Name](../BalloonStyle/BalloonStyle_Name.md) | Gets/Sets the name of the Style. |
| [Parent](../BalloonStyle/BalloonStyle_Parent.md) | Property returning the parent of this object. |
| [Properties](../BalloonStyle/BalloonStyle_Properties.md) | Property that gets and sets the properties to display in the balloon. The number of properties displayed depends on the balloon shape. |
| [ScaleToTextHeight](../BalloonStyle/BalloonStyle_ScaleToTextHeight.md) | Property that gets and sets whether to define the balloon size by text height. This property is not applicable if the balloon type is kNoneBalloonType or kLinearBalloonType. |
| [StretchBalloonToText](../BalloonStyle/BalloonStyle_StretchBalloonToText.md) | Property that gets and sets whether to size the balloon horizontally to accommodate long text strings. If set to False, the balloon is restricted to the defined size. This property is not applicable if the balloon type is kNoneBalloonType or kLinearBalloonType. |
| [StyleLocation](../BalloonStyle/BalloonStyle_StyleLocation.md) | Property that returns the location of this style, i.e. local to the document, cached locally in the document, exists in the library. Styles that exist in the library cannot be edited. |
| [StyleType](../BalloonStyle/BalloonStyle_StyleType.md) | Gets the type of the style. |
| [TextStyle](../BalloonStyle/BalloonStyle_TextStyle.md) | Property that gets and sets the text style used to format the text in a balloon. |
| [Type](../BalloonStyle/BalloonStyle_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UpToDate](../BalloonStyle/BalloonStyle_UpToDate.md) | Property that gets the up-to-date status of the style against the global repository. |

## Accessed From

[Balloon.Style](../Balloon/Balloon_Style.md), [BalloonStylesEnumerator.Item](../BalloonStylesEnumerator/BalloonStylesEnumerator_Item.md), [ObjectDefaultsStyle.BalloonStyle](../ObjectDefaultsStyle/ObjectDefaultsStyle_BalloonStyle.md)

## Version

Introduced in version 2009

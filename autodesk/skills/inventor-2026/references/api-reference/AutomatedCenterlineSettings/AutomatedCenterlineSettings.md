# AutomatedCenterlineSettings Object

## Description

The AutomatedCenterlineSettings object provides access to all of the settings that are used when automatically generating centerlines and center marks.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../AutomatedCenterlineSettings/AutomatedCenterlineSettings_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [ApplyToBends](../AutomatedCenterlineSettings/AutomatedCenterlineSettings_ApplyToBends.md) | Gets and sets if centerlines and center marks should be placed on sheet metal Bend features. |
| [ApplyToCircularPatterns](../AutomatedCenterlineSettings/AutomatedCenterlineSettings_ApplyToCircularPatterns.md) | Gets and sets if centerlines and center marks should be placed on circular pattern features. |
| [ApplyToCylinders](../AutomatedCenterlineSettings/AutomatedCenterlineSettings_ApplyToCylinders.md) | Gets and sets if centerlines and center marks should be placed on cylindrical faces. |
| [ApplyToFillets](../AutomatedCenterlineSettings/AutomatedCenterlineSettings_ApplyToFillets.md) | Gets and sets if centerlines and center marks should be placed on Fillet features. |
| [ApplyToHoles](../AutomatedCenterlineSettings/AutomatedCenterlineSettings_ApplyToHoles.md) | Gets and sets if centerlines and center marks should be placed on Hole features. |
| [ApplyToPunches](../AutomatedCenterlineSettings/AutomatedCenterlineSettings_ApplyToPunches.md) | Gets and sets if centerlines and center marks should be placed on sheet metal Punch features. |
| [ApplyToRectangularPatterns](../AutomatedCenterlineSettings/AutomatedCenterlineSettings_ApplyToRectangularPatterns.md) | Gets and sets if centerlines and center marks should be placed on rectangular pattern features. |
| [ApplyToRevolutions](../AutomatedCenterlineSettings/AutomatedCenterlineSettings_ApplyToRevolutions.md) | Gets and sets if centerlines and center marks should be placed on Revolved features. |
| [ApplyToSketches](../AutomatedCenterlineSettings/AutomatedCenterlineSettings_ApplyToSketches.md) | Gets and sets if centerlines and center marks should be placed on circular and elliptical geometry within sketches. |
| [ApplyToWorkFeatures](../AutomatedCenterlineSettings/AutomatedCenterlineSettings_ApplyToWorkFeatures.md) | Gets and sets if centerlines and center marks should be placed on visible work features. |
| [ArcAngleThreshold](../AutomatedCenterlineSettings/AutomatedCenterlineSettings_ArcAngleThreshold.md) | Gets and sets the minimum angle for creating a center mark or centerline on circles, arcs, or ellipses. |
| [CircularEdgeMaximumThreshold](../AutomatedCenterlineSettings/AutomatedCenterlineSettings_CircularEdgeMaximumThreshold.md) | Gets and sets the maximum radius of a circular edge that centerlines and center marks should be placed on. |
| [CircularEdgeMinimumThreshold](../AutomatedCenterlineSettings/AutomatedCenterlineSettings_CircularEdgeMinimumThreshold.md) | Gets and sets the minimum radius of a circular edge that centerlines and center marks should be placed on. |
| [FilletRadiusMaximumThreshold](../AutomatedCenterlineSettings/AutomatedCenterlineSettings_FilletRadiusMaximumThreshold.md) | Gets and sets the maximum radius of a fillet that centerlines and center marks should be placed on. |
| [FilletRadiusMinimumThreshold](../AutomatedCenterlineSettings/AutomatedCenterlineSettings_FilletRadiusMinimumThreshold.md) | Gets and sets the minimum radius of a fillet that centerlines and center marks should be placed on. |
| [ProjectionNormalAxis](../AutomatedCenterlineSettings/AutomatedCenterlineSettings_ProjectionNormalAxis.md) | Gets and sets if centerlines should be created where the entity axis is normal to the drawing view plane. |
| [ProjectionParallelAxis](../AutomatedCenterlineSettings/AutomatedCenterlineSettings_ProjectionParallelAxis.md) | Gets and sets if centerlines should be created where the entity axis is parallel to the drawing view plane. |
| [RadiusThresholdPrecision](../AutomatedCenterlineSettings/AutomatedCenterlineSettings_RadiusThresholdPrecision.md) | Gets and sets the number of decimal accuracy to use for comparing the size of fillets, arcs and circular features to the threshold. |
| [Type](../AutomatedCenterlineSettings/AutomatedCenterlineSettings_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[DetailDrawingView.GetAutomatedCenterlineSettings](../DetailDrawingView/DetailDrawingView_GetAutomatedCenterlineSettings.md), [DrawingSettings.AutomatedCenterlineSettings](../DrawingSettings/DrawingSettings_AutomatedCenterlineSettings.md), [DrawingSketch.GetAutomatedCenterlineSettings](../DrawingSketch/DrawingSketch_GetAutomatedCenterlineSettings.md), [DrawingView.GetAutomatedCenterlineSettings](../DrawingView/DrawingView_GetAutomatedCenterlineSettings.md), [SectionDrawingView.GetAutomatedCenterlineSettings](../SectionDrawingView/SectionDrawingView_GetAutomatedCenterlineSettings.md)

## Version

Introduced in version 2010

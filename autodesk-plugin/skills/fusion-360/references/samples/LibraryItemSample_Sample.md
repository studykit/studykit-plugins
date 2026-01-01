# Library Item API Sample

## Description

Demonstrates how to examine library items using the API.

To use the sample, create a new Python or C++ script and copy and paste this code, replacing the existing default code. The script will search for and record all components and library items in the current project. They are displayed in a dialog when the script has finished.

## Code Samples

* [C++](#C++)
* [Python](#Python)

|  |
| --- |
| Copy Code |

```
// We will activate the Design Environment before identifying components and/or library items if they exist.
// Library items are commonly used components such as fasteners that may include nuts, bolts, washers and screws.
// They may be utilised across many projects, especially those including assemblies.

#include <Core/CoreAll.h>
#include <Fusion/FusionAll.h>

using namespace adsk::core;
using namespace adsk::fusion;

Ptr<Application> app;
Ptr<UserInterface> ui;

// Function to concatenate a list of strings punctuated by linefeeds into a single string.
std::string concatenateStrings(const std::vector<std::string>& stringList)
{
    std::string concatenatedString;
    for (const auto& str : stringList)
    {
        concatenatedString += str + "\n";
    }
    return concatenatedString;
}

extern "C" XI_EXPORT bool run(const char* context)
{
    // Initialisation.
    app = Application::get();
    if (!app)
        return false;

    ui = app->userInterface();

    // Ensure we are in the Design environment.
    Ptr<Workspace> designWorkspace = ui->workspaces()->itemById("FusionSolidEnvironment");
    if (ui->activeWorkspace() != designWorkspace)
    {
        designWorkspace->activate();
    }

    // Assume initially we have no library components.
    std::string resultMessage = "This design has no library items.";
    std::string resultText = resultMessage;
    std::string indent1 = "      ";
    std::string indent2 = "\t";

    // Initialise a list of non - library components with a heading.
    std::vector<std::string> nonlib = {"Components"};

    // Initialise a list of library item components with a heading.
    std::vector<std::string> output = {"Library Components"};

    Ptr<Design> design = app->activeProduct();
    if (design)
    {
        // Get the 'LibraryItem' property group in the root component of the design.

        auto allComponents = design->allComponents();
        auto allCompCount = allComponents->count();

        // Iterate over all components.
        for (auto i = 0; i < allCompCount; ++i)
        {
            auto component = allComponents->item(i);

            // Concentrate first on library items.
            if (component->isLibraryItem())
            {
                // Capture and indent the component name.
                output.push_back(indent1 + component->name());

                // Get a list of available library items.
                auto propertyGroups = component->propertyGroups();
                auto groupLibraryItem = propertyGroups->itemById("libraryItem");

                // Iterate over all library items.
                auto countLibProps = groupLibraryItem->count();
                for (int j = 0; j < countLibProps; ++j)
                {
                    auto property = groupLibraryItem->item(j);
                    auto propName = property->name();

                    // Get string value from string property.
                    auto stringProperty =
                        static_cast<StringProperty*>(property->queryInterface(StringProperty::classType()));
                    output.push_back(indent2 + propName + " = " + stringProperty->value());
                }
                // Provide an extra linebreak.
                output.push_back(indent1);
            }
            else
            {
                // Indent the names of any non - library items.
                nonlib.push_back(indent1 + component->name());
            }
        }
        // Overwrite our reassuring message with the results if there are any.
        if ((std::size(output) > 1) || (std::size(nonlib) > 2))
        {
            resultText = concatenateStrings(nonlib);
            resultText += "\n";
            resultText += concatenateStrings(output);

            resultMessage = "The results are displayed in the TEXT COMMANDS window.";
        }
        Ptr<TextCommandPalette> textPalette = ui->palettes()->itemById("TextCommands");
        if (!textPalette->isVisible())
        {
            textPalette->isVisible(true);
            adsk::doEvents();
        }
        app->log(resultText);

        // Indicate in a messageBox that the script has finished
        ui->messageBox(
            resultMessage,
            "Library Items Sample\t\t\t\t\t",
            MessageBoxButtonTypes::OKButtonType,
            MessageBoxIconTypes::InformationIconType);
    }

    return true;
}
```

|  |
| --- |
| Copy Code |

```
# We will activate the Design Environment before identifying components and/or library items if they exist.
# Library items are commonly used components such as fasteners that may include nuts, bolts, washers and screws.
# They may be utilised across many projects, especially those including assemblies.

import adsk.core, adsk.fusion, traceback

def run(context):
    ui = None
    try:

        # Initialisation.
        app = adsk.core.Application.get()
        ui  = app.userInterface

        # Ensure we are in the Design environment.
        designWorkspace: adsk.core.Workspace = ui.workspaces.itemById("FusionSolidEnvironment")
        if ui.activeWorkspace != designWorkspace:
            designWorkspace.activate()

        # Assume initially we have no library components.
        resultMessage = 'This design has no library items.'
        resultText = resultMessage
        indent1 = '        '
        indent2 = '\t'
        messageBoxLineLimit = 25

        # Initialise a list of non-library components with a heading.
        nonlib: list[str] = ['Components']

        # Initialise a list of library item components with a heading.
        output: list[str] = ['Library Components']

        design = adsk.fusion.Design.cast(app.activeProduct)
        if design:

            # Get the 'LibraryItem' property group in the root component of the design.
            allComponents: adsk.fusion.Components = design.allComponents

            # Iterate over all components.
            for i in range(allComponents.count):
                component: adsk.fusion.Component = allComponents.item(i)

                # Concentrate first on library items.
                if component.isLibraryItem:

                    # Capture and indent the component name.
                    output.append(f'{indent1}{component.name}')

                    # Get a list of available library items.
                    propertyGroups: adsk.core.PropertyGroups = component.propertyGroups
                    groupLibraryItem: adsk.core.PropertyGroup = propertyGroups.itemById('libraryItem')

                    # Iterate over all library items.
                    for j in range(groupLibraryItem.count):
                        property: adsk.core.Property = groupLibraryItem.item(j)

                        # Get string value from string property.
                        stringProperty = adsk.core.StringProperty.cast(property)
                        output.append(f'{indent2}{property.name}  = {stringProperty.value}')

                    # Provide an extra linebreak.
                    output.append(indent1)
                else:
                    # Indent the names of any non-library items.
                    nonlib.append(f'{indent1}{component.name}')

        # Overwrite our reassuring message with the results if there are any.
        if len(output) > 1 or len(nonlib) > 2:
            resultLines = nonlib + [indent1] + output
            resultMessage = '\n'.join(resultLines[0:messageBoxLineLimit])
            if len(resultLines) >= messageBoxLineLimit:
                resultMessage += '\n...\n\nThe full results are displayed in the TEXT COMMANDS window.'
            resultText = '\n'.join(resultLines)

        # Display our full conclusions in the text palette
        textPalette = ui.palettes.itemById('TextCommands')
        if not textPalette.isVisible:
            textPalette.isVisible = True
            adsk.doEvents()
        app.log(resultText)

        # Display our possibly truncated conclusions in a messageBox.
        ui.messageBox(
            resultMessage,
            'Library Items Sample' + indent2 * 5,
            adsk.core.MessageBoxButtonTypes.OKButtonType,
            adsk.core.MessageBoxIconTypes.InformationIconType)

    # Capture and highlight any reason for error
    except Exception as e:
        if ui:
            ui.messageBox(
                f'Failed: {e}\n{format(traceback.format_exc())}',
                'Unable to continue',
                adsk.core.MessageBoxButtonTypes.OKButtonType,
                adsk.core.MessageBoxIconTypes.CriticalIconType)
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
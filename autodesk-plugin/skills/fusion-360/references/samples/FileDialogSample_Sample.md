# File Dialog Sample

## Description

Demonstrating how to pop up a file dialog and a folder dialog.

## Code Samples

* [C++](#C++)
* [Python](#Python)

|  |
| --- |
| Copy Code |

```
#include <Core/Application/Application.h>
#include <Core/UserInterface/UserInterface.h>
#include <Core/UserInterface/FileDialog.h>
#include <Core/UserInterface/FolderDialog.h>

using namespace adsk::core;

Ptr<UserInterface> ui;

extern "C" XI_EXPORT bool run(const char* context)
{
    Ptr<Application> app = Application::get();
    if (!app)
        return false;

    ui = app->userInterface();
    if (!ui)
        return false;

    std::string msg("");

    // Set styles of file dialog.
    Ptr<FileDialog> fileDlg = ui->createFileDialog();
    if (!fileDlg)
        return false;
    fileDlg->title("Fusion File Dialog");
    fileDlg->filter("*.*");
    fileDlg->isMultiSelectEnabled(true);

    // Show file open dialog
    DialogResults dlgResult = fileDlg->showOpen();
    if (dlgResult == DialogOK)
    {
        msg += "\nFiles to Open:";
        std::vector<std::string> fileNames = fileDlg->filenames();
        for (std::string fileName : fileNames)
        {
            msg += "\n\t" + fileName;
        }
    }
    else
    {
        return false;
    }

    // Show file save dialog
    fileDlg->title("Fusion Save File Dialog");
    dlgResult = fileDlg->showSave();
    if (dlgResult == DialogOK)
    {
        std::string fileName = fileDlg->filename();
        msg += "\nFile to Save: " + fileName;
    }
    else
    {
        return false;
    }

    // Set styles of file dialog.
    Ptr<FolderDialog> folderDlg = ui->createFolderDialog();
    if (!folderDlg)
        return false;
    folderDlg->title("Fusion Choose Folder Dialog");

    // Show folder dialog
    dlgResult = folderDlg->showDialog();
    if (dlgResult == DialogOK)
    {
        std::string folderName = folderDlg->folder();
        msg += "\nSelected Folder: " + folderName;
    }
    else
    {
        return false;
    }

    if (!msg.empty())
        ui->messageBox(msg);
    return true;
}
```

|  |
| --- |
| Copy Code |

```
import adsk.core, adsk.fusion, traceback
import os.path

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface

        msg = ''
        # Set styles of file dialog.
        fileDlg = ui.createFileDialog()
        fileDlg.isMultiSelectEnabled = True
        fileDlg.title = 'Fusion Open File Dialog'
        fileDlg.filter = '*.*'

        # Show file open dialog
        dlgResult = fileDlg.showOpen()
        if dlgResult == adsk.core.DialogResults.DialogOK:
            msg += '\nFiles to Open:'
            for filename in fileDlg.filenames:
                msg += '\n\t{}'.format(filename)
        else:
            return

        # Show file save dialog
        fileDlg.title = 'Fusion Save File Dialog'
        dlgResult = fileDlg.showSave()
        if dlgResult == adsk.core.DialogResults.DialogOK:
            msg += '\nFile to Save: {}'.format(fileDlg.filename)
        else:
            return

        # Set styles of file dialog.
        folderDlg = ui.createFolderDialog()
        folderDlg.title = 'Fusion Choose Folder Dialog'

        # Show folder dialog
        dlgResult = folderDlg.showDialog()
        if dlgResult == adsk.core.DialogResults.DialogOK:
            msg += '\nSelected Folder: {}'.format(folderDlg.folder)
        else:
            return

        ui.messageBox(msg)

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |